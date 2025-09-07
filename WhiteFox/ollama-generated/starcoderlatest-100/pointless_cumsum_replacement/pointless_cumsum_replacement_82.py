
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tensor = torch.full([1, 2], 1, dtype=torch.float32, layout=torch.strided, device=torch.device("cpu"), pin_memory=False)

    def forward(self):
        t1 = torch.full([1, 2], 1, dtype=torch.float32, layout=torch.strided, device=torch.device("cpu"), pin_memory=False)
        t2 = convert_element_type(t1, torch.float32)
        t3 = torch.cumsum(t2, 1)
        return t3


# Initializing the model
m = Model()

# Input to the model
x = torch.randn(10, 2, dtype=torch.float32, layout=torch.strided, device=torch.device("cpu"), pin_memory=False)
