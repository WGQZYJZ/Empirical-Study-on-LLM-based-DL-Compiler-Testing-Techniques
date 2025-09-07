
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convert_element_type = torch.nn.ConvertElementType()

    def forward(self, x1):
        t1 = torch.full([x1.shape[0], 48], 1, dtype=torch.float32)
        t2 = convert_element_type(t1, torch.int64)
        t3 = torch.cumsum(t2, 1)

        return t3
# Initializing the model
m = Model()


