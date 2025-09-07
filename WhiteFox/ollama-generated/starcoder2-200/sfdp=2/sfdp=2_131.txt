
import torch
import numpy as np
class Model(torch.nn.Module):
    def __init__(self, inputSize, outputSize):
        super().__init__()
        self.dense1  = torch.nn.Linear(inputSize, outputSize)
 
    def forward(self, x2):
        r2_out1  = self.dense1(x2).clone() 
        r2_out3  = r2_out1.softmax(-1) # Apply the softmax to the input
        r2_out4  = torch.nn.functional.dropout(r2_out3, p=0.75) # Apply dropout with a probability of 0.75
        r2_out6  = torch.nn.functional.dropout(torch.randn(1), p=0.8) 
        r2_out9  = r2_out4.matmul(r2_out6).clone() 
        return r2_out9
