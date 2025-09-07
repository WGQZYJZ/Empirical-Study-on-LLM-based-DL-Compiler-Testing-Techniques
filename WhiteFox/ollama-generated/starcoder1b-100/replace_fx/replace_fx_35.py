
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        return (
            lowmem_dropout(input_tensor)  # Dropout is the original implementation of `torch.nn.functional.dropout`.
                .permute(...) # Permute the input tensor
        )


# Initializing the model
m = Model()

