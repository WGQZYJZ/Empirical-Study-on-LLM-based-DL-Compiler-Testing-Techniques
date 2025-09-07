

class MyModel(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
 
        self._linear = torch.nn.Linear(3, 4)
 
    def forward(self, inputs):
        outputs = self._linear(inputs)
 
        return outputs
