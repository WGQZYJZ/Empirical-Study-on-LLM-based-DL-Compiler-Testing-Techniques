
import torch

class ScaledDotProductAttention(torch.nn.Module):
    def __init__(self, inv_scale=1.0):
        super().__init__()
        self.softmax = torch.nn.Softmax(-1)

    def forward(self, query, key, value):
        scaled_dot_product  = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = self.softmax(scaled_dot_product) 
        output = attention_weights.matmul(value)

        return output

class Model(torch.nn.Module):
    def __init__(self, inv_scale=0.7943285121363527):
        super().__init__()
        self.scaled_dot_product = ScaledDotProductAttention()

    def forward(self, query, key, value):
       output  = self.scaled_dot_product(query, key, value) 
       return output


model = Model().cuda()

input1  = torch.randn(2, 4096).float().cuda()
input2  = torch.randn(2, 512, 7, 7).float().cuda()

input3  = torch.randn(2, 512, 8, 8).float().cuda()

input4  = torch.randn(2, 4096).float().cuda()

__output__  = model(input1, input2, input3)

