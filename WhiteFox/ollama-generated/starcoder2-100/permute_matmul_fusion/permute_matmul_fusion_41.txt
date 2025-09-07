
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 3)
        self.linear2 = torch.nn.Linear(3, 5)

    def forward(self, x1):
        v0  = input_tensor.permute(...).cuda() # Permute the input tensor A. Convert the tensor to GPU
        v1 = torch.bmm(v0, self.linear2.weight.t().contiguous()) + self.linear2.bias.view(-1, 5) 
        return v1


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(3, 4).cuda() # The tensors will be on GPU after invoking the permute method with 'permute(...)' in PyTorch
__output__  = m(x1)

