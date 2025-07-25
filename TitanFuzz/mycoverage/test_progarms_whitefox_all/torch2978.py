import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()
        d_model, nhead = config.d_model, config.nhead
        self.scale_factor = 1 / (d_model ** 0.5)
        self.dropout_p = 0.1
 
    def forward(self, x1, x2):
        qk = torch.matmul(x1, x2.transpose(-2, -1))
        scaled_qk = qk.mul(self.scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = F.dropout(softmax_qk, p=self.dropout_p)
        output = dropout_qk.matmul(x2)
        return output

m = Model()
# Initializing the model
config = Config()
m = Model(config)

# Inputs to the model
x1 = torch.randn(2052, 12, 128)
x2 = torch.randn(2052, 12, 128)
