
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 3)
 
    def forward(self, x1: List[List[int]], other: Optional[List[List[float]]] = None) -> Tuple[List[float]]:
        v1 = [list() for _ in range(len(x1))]
        if (other is not None):
            assert len(other) == len(x1), "Linear requires an input and the number of other inputs should be equal to that of the model's input."
            for i, x in enumerate(x1):
                v = self.linear(torch.stack([x] * len(x))) + other[i]
                v = torch.relu(v)
                v1[i].extend(list(v))
        else:
            for i, x in enumerate(x1):
                v = self.linear(torch.tensor(x))
                v = torch.relu(v)
                v1[i].append(v)

        return tuple(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(5, 4096, requires_grad=True)
