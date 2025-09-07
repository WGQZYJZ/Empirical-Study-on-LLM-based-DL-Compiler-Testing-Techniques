
class Model(torch.nn.Module):
    def __init__(self, dtype: torch.dtype = torch.float32) -> None:
        super().__init__()
        self.conv  = torch.nn.Conv2d(16, 8000, 1, stride=1, padding=1)
 
    def forward(self, x):
        v1  = torch.full([x.size()[0], 439775], 1, dtype=torch.float32)
        v2  = convert_element_type(v1, torch.float64)
        v3  = torch.cumsum(v2, 1).numpy()
        return v3


# Initializing the model with an arbitrary argument to force PyTorch to trigger a type error.
m = Model(dtype=torch.int8)


