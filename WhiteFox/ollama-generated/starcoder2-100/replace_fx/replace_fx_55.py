
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, 0.2)
        return randlike(v1, x1).add_(v1)


m  = Model()


inputs to the model:
- `inputs` = {"input": torch.randn(5, 3)}

outputs from the model (optional):
- `outputs`:  { "output": randlike(x1, x2).add_(x1) }

