
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input_tensor):
        v1 = torch.full([1, 2], 0, dtype=torch.float32)
        v2 = convert_element_type(v1, torch.int64)
        v3 = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m = Model()


