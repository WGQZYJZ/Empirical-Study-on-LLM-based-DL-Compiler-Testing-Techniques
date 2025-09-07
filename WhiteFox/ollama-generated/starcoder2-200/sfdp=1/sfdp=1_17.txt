

import torch

class Model(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.key = torch.nn.Linear(1024, 768)

    def forward(self, query, key, value):
       v1 = torch.matmul(query, self.key(key).transpose(-2,-1)) # Compute the dot product of the query and key tensors
       v3 = v1 / 5.0 # Scale the dot product by an inverse scale factor
       v4 = v3.softmax(dim=-1) # Apply softmax to the scaled dot product
       dropout_qk = torch.nn.functional.dropout(v4, p=2.0) 
       v6 = dropout_qk.matmul(value) # Compute the dot product of the dropout output and the value tensor
       return v6

