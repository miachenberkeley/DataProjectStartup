# -*- coding: utf-8 -*-
# Natural Language Toolkit: Machine Translation
#
# Copyright (C) 2001-2016 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>, Tah Wei Hoon <hoon.tw@gmail.com>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

"""
Experimental features for machine translation.
These interfaces are prone to change.
"""

from nltkx.translate.api import AlignedSent, Alignment, PhraseTable
from nltkx.translate.ibm_model import IBMModel
from nltkx.translate.ibm1 import IBMModel1
from nltkx.translate.ibm2 import IBMModel2
from nltkx.translate.ibm3 import IBMModel3
from nltkx.translate.ibm4 import IBMModel4
from nltkx.translate.ibm5 import IBMModel5
from nltkx.translate.bleu_score import sentence_bleu as bleu
from nltkx.translate.ribes_score import sentence_ribes as ribes
from nltkx.translate.metrics import alignment_error_rate
from nltkx.translate.stack_decoder import StackDecoder
