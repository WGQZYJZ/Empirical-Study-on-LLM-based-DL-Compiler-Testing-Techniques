
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d(...)

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, ...)
        t1 = torch.rand_like(v1)  # This will not be replaced by the lowmem_dropout method if the model is running on a CPU device
        v2 = self.dropout(v1) 
        return v2

# Initializing the model
m = Model()


