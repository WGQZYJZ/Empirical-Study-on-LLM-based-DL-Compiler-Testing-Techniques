
import torch

class Model(torch.nn.Module):
    def __init__(self, hiddensize=1024):
        super().__init__()
        self._dropout = 0.5 
        self.input_proj = torch.nn.Linear(hiddensize + 768, hiddensize) # This is a linear transformation from the sum of the sequence length and 768 to the sequence length
        self.output_proj = torch.nn.Linear(hiddensize, 1024) # The output layer, which will be transformed by dropout from size 1024 to size 512
    
    def forward(self, input_ids=None, mask=None):

        query  = torch.softmax(self.input_proj(input_ids), dim=-1) * self._dropout
        keys  = torch.softmax(query + mask).transpose(-2,-1)
        values = torch.ones([keys.size()[-3], 50, 768])
        return query @ keys @ values

