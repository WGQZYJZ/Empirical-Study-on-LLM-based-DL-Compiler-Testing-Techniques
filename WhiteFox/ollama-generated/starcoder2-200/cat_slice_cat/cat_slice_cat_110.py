
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, inputs):
        v0 = torch.tensor([[8], [7]], dtype=int) # Initializing the 2D tensor as int type and setting the size of each dimension to `[8][7]`.
        v1 = v0[:, :, None].expand_as(inputs[0]) + inputs[1][:, None]
        v2 = torch.cat([v1[:, :3], v1[:, 5:]], dim=1) # Concatenating the concatenated tensor along dimension 1
        return v2


# Initializing the model and setting input tensors for the model. 
m  = Model()
inputs = [torch.randn(4, 7), torch.randn(3, 6)]
 
__output__  = m(inputs) # Feeding the initial input tensor to the model

