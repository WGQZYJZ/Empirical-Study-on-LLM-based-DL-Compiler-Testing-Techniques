
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
    
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = torch.tanh(v1)
         return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
 
 # Forward pass through the network for validation
 __output__= m(x1)

# Generating a test case to fuzz. A test case is described as a dictionary, 
# where keys are PyTorch tensors and values are the respective outputs of the tensor.
import torch
from typing import Dict

def get_test_case() -> Dict[torch.Tensor, torch.Tensor]:
    input1 = torch.randn(2048)

    input_dict: Dict[str, torch.Tensor]  = {} # The key should be the name of the input. In the previous example it is 'x'
    input_dict['input'] = input1
 
    model = Model()
    output = m(**input_dict)
    return {input1: output}

# Runing the fuzzer to find an adversarial example.
import torch
from typing import Dict

 # The input of the fuzzed function is a dictionary with keys corresponding to 
# the model input names and values for each key being the respective input tensors to be fuzzed with.
 # The key should be the name of the input. In the previous example it is 'x'
# Also, please include the outputs in the return statement of the fuzzer function so that they can 
# be validated after fuzzing. This makes the testing phase easy to implement for the user. 
# If this is not provided, we have to provide an assertion to check whether the output is as expected or not. 
def fuzz(inputs):
    model = Model()
    outputs = m(**inputs)
    return {**inputs,'outputs':outputs}

from fuzzy_testing import find_adversarial_example
  # Call find_adversary function with:
  # - the target torch script module to be attacked. 
  # - a dictionary containing the input name (as keys), and their shape as values. The value can also be an array of shapes for different scenarios where the model takes multiple inputs.
  # - the fuzzer which generates inputs to the target model for testing
results = find_adversarial_example(m,  {'inputs': torch.Size([2048])}, fuzz)
