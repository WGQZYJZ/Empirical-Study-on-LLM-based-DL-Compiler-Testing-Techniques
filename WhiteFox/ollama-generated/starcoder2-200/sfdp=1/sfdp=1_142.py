
import torch

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      q = self._get_queries(x1) # Compute the query tensor from the input
      k = self._get_keys(q)  # Compute the key tensor from the input
      v = self.linear(k).softmax() 
      return q + v

    def _get_queries(self, x):
        raise NotImplementedError

    def _get_keys(self, query):
        raise NotImplementedError

m = Model()


inputs1 = torch.randn((320, 8)) # Inputs to the model
inputs2 = torch.randn((64, 512)) # Inputs to the model
