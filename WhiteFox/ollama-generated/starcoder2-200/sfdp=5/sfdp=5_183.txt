
import torch.nn.functional as F
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1, input2):
        v0 = F.linear(input1, weight=None) # Compute the dot product of two 1D tensors with broadcasting
        v1 = torch.sin(v0 + 5) * 3 / input1
        v2 = -F.relu(-torch.cos(v1)) + 100
        return v2

# Initializing the model
model = Model()

 # Input to the model (random tensors with shape [batch_size, seq_length] and [seq_length])
input1 = torch.randn([4,8])
input2 = torch.randn(8)
output = model(input1, input2)