
class Model(torch.nn.Module):
    def __init__(self, device="cpu", layout="NCDHW"):
        super().__init__()
        self.device = torch.device(device)
 
    def forward(self, arg1, arg2): 
        t0 = torch.full([arg1, arg2], 1, dtype=torch.float32, layout=layout, device=self.device, pin_memory=False) # Create a tensor filled with the scalar value 1
        t1 = torch.ops.aten._convert_element_type(t0, torch.int64) # Convert the elements of the tensor to int64 dtype
        return torch.cumsum(t1, 1).detach().to(self.device), (224, 384)


# Initializing the model
m = Model()

