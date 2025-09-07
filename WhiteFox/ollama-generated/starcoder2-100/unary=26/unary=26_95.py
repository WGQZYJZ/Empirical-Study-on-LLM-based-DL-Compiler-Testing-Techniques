import unittest
from helper import compare_inputs_outputs

 # Inputs to the model 
 x1 = torch.randn(1, 32768)
  __output__  = m(x1)

 compare_inputs_outputs(__output__, 0, 'm(x1)', x1)

