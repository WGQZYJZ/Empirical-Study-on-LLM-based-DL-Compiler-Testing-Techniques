
class Model(torch.nn.Module):
    def __init__(self, dtype, layout, device):
        super().__init__()
        self.t = torch.full([4], 1, dtype=dtype, layout=layout, device=device, pin_memory=False)
 
    def forward(self):
        v1 = torch.cumsum(self.t, 0) # Compute the cumulative sum of all elements in the tensor along dimension 0
        return v1


# Initializing the model
m = Model(torch.float32, 'CHW', torch.device('cpu'))

