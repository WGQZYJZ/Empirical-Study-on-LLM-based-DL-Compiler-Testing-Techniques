import torch
from torch import nn

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.norm = torch.tensor([[[-1.80617e-05, -7.39575e-06, -7.06623e-06], [-0.000550219, 0.00403799, -0.00134023], [3.61908e-05, 0.000207546, 1.74391e-06]], [[-5.35324e-05, 0.000382519, -0.0006293], [0.00057971, -0.00129052, 0.000362418], [-7.42216e-05, -4.96203e-05, 0.000555206]], [[0.000335804, 0.00222172, 0.000405405], [-0.000405796, -0.00212755, -0.000933267], [0.00149076, 0.0022295, 0.000161554]], [[-0.000358775, -0.000110063, -0.000298915], [0.000724923, 0.00116608, 0.000747272], [0.000415906, -0.000472659, -0.000734964]], [[0.000176228, 9.28977e-05, 0.000294339], [-0.00011753, 0.000933664, -0.00014085], [9.46786e-05, -2.14582e-06, 3.53265e-05]], [[0.000223743, -0.000153491, 0.000274413], [-0.000260172, 0.000109985, -0.000409414], [0.000310485, 0.000383859, -0.000182654]], [[-3.39694e-05, 0.000147813, 0.000545507], [0.000256115, 0.000976401, -7.32397e-05], [7.7917e-05, 0.000422021, 0.000187096]]])
        self.q = torch.randn(1, 8, 4)
        self.k = torch.randn(1, 8, 4)
        self.v = torch.randn(1, 8, 4)
        self.inv_scale_factor = 0.5
        self.dropout_p = 0.0
 
    def forward(self, q, k, v):
        qk = torch.matmul(q, k.transpose(-2, -1))
        scaled_qk = qk.div(inv_scale_factor)
        softmax_qk = scaled_qk.softmax(dim=-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)
        output = dropout_qk.matmul(v)
        return output

m = Model()
# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(1, 8, 4)
k = torch.randn(1, 8, 4)
v = torch.randn(1, 8, 4)
