
class Model(torch.nn.Module):
    def __init__(self, replace_fx=False):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

        if replace_fx:
            self._lowmem_dropout = lowmem_dropout
            self._randlike = rand_like

    def forward(self, x1):
        # If we have no GPU device available, it is fine to not run the following lines
        x1.cuda()  # Re-use previous model

        v1 = x1.permute(0, 2, 1)
        if self._lowmem_dropout:
            # Run lowmem dropout and make a copy of the permuted tensor.
            # We keep it around as input so that we can reuse the memory for other ops later.
            # However, since we are doing this in place, we only copy the data from `input` to our output `v2`, but not the original `v1`.
            v2 = self._lowmem_dropout(input=v1)
            return v2
        else:
            v2 = torch.rand_like(v1)

        v3 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Running the model with default configuration and input values
__output = m(torch.randn(1, 2, 2))  # Output is generated on CPU device

