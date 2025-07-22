import os
import torch
import torch.nn.functional as F
import torch.nn as nn
import numpy as np
from torch.autograd import Variable
import math
import torch as th
import torch.linalg as la
from torch.nn import Parameter
import torch.linalg as linalg



func = ().to('cuda')


sequence_length = 10


sequence_length = 10




attn_mask = torch.tril(torch.ones((sequence_length, sequence_length)))



embedding_size = 32


sequence_length = 10


batch_size = 1


xquery = torch.randn(batch_size, sequence_length, embedding_size)



embedding_size = 32


sequence_length = 10


batch_size = 1


xkey = torch.randn(batch_size, sequence_length, embedding_size)



embedding_size = 32


sequence_length = 10


batch_size = 1


xvalue = torch.randn(batch_size, sequence_length, embedding_size)


test_inputs = [attn_mask, xquery, xkey, xvalue]
