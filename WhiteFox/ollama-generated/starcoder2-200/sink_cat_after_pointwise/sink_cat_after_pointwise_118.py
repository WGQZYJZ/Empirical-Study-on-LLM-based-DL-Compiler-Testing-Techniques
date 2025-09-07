
class Model(torch.nn.Module):
    def __init__(self, batchsize=None, dim=None):
        super().__init__()

        # Shape of tensors and number of batches for each tensor
        self._batch = 1 if not isinstance(batchsize, int) else max(batchsize - 50 + 1, 1)
        self.dim   = torch.nn.Parameter(torch.randint(20, 30, size=(self._batch,)))

        # Initialize the model
        self.linear = torch.nn.Linear(
            in_features=int(self.dim), 
            out_features=int(self.dim) + batchsize - 1)

    def forward(self, *inputs): 
        t1 = inputs[0].permute(0, dim)

        # Make sure the permute operation is done before concatenation
        if dim != self._batch and isinstance(*inputs, (torch.nn.ParameterList, tuple)):
            t2  = torch.cat([*inputs], dim=self._batch)

        return self.linear(t1)

# Initializing the model
m = Model()
__output__  = m(*inputs)

