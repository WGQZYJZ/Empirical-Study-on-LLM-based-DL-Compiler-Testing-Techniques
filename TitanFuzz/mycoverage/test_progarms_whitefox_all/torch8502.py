import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, query, key, value, inv_scale_factor, dropout_p):
        qk = torch.matmul(query, key.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(value)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
query = torch.tensor([[[[1.], [1.]],
                        [[1.], [1.]],
                        [[1.], [1.]],
                        [[1.], [1.]]]]).float()
key = torch.tensor([[[[[1.], [1.], [1.], [1.], [1.]],
                       [[1.], [1.], [1.], [1.], [1.]]
                       ]]]).float()
value = torch.tensor([[[[[0.], [1.], [-1.], [1.], [1.]],
                         [[1.], [1.], [1.], [-1.], [1.]],
                         [[1.], [1.], [-1.], [1.], [1.]],
                         [[1.], [1.], [1.], [1.], [1.]],
                         [[0.1], [1.], [-1.], [1.], [1.]]]
                        ]]).float()
