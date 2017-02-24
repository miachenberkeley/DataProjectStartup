clear all;clc;close all;

doSoftMax   = false;
doReLU      = false;
lambda      = .0001;

checkNNgradients(lambda,doSoftMax,doReLU)


[features,labels,posterior] = construct_data(300,'train','nonlinear');
%% drop the constant term
X = features([1,2],:)';
%% labels change from 0,1 to 1,2 (required by the code below)
y = labels' + 1;
m = size(X, 1);

%% Specify network architecture
%% format: input dimension, # hidden notes at different layers, output dimension
nnodes =  [2,50,2];

%% initialize network parameters to random value
randn('seed',0); % (but make it repeatable)

nHidden    = length(nnodes)-1;
initial_value = [];
for l=1:nHidden,
    %% add one for the constant component
    n_inputs        = nnodes(l) + 1;
    %% target neurons
    n_outputs       = nnodes(l+1);
    
    %% standard deviation of Gaussian distribution used for initialization
    sigma           = .1;
    WeightsLayer    = randn(n_inputs,n_outputs)*sigma;
    
    %% collate everything in one big parameter vector
    initial_value  = [initial_value;WeightsLayer(:)];
end

%% optimizer options
options = optimset('MaxIter', 500);

%% our optimization function (mincg) requres creating a pointer to
%% the function that is being minimized
costFunction = @(p) nnet(p, ...
    nnodes, X, y, lambda,...
    doSoftMax,doReLU);

[nn_params, cost] = fmincg(costFunction, initial_value, options);


if 0
    pred = nnet(nn_params,nnodes, X,[],[],doSoftMax,doReLU);
    fprintf('\nTraining Set Accuracy: %f\n', mean(double(pred == y)) * 100);
end
loc_x = [0:.01:1];
loc_y = [0:.01:1];
[grid_x,grid_y] = meshgrid(loc_x,loc_y);
Xs      = [grid_x(:), grid_y(:)];
[sv,sh] = size(grid_x);
pred = nnet(nn_params,nnodes, Xs,[],[],doSoftMax,doReLU);
pred = pred(:,1);
figure,
imshow(reshape(pred,[sv,sh]),[])



