
class Model(torch.nn.Module):
    def __init__(self, config={}):
        super().__init__()
        # config is passed to the nn.functional.dropout function
        self.linear = torch.nn.Linear(..., ..., fallback_random=config["fallback_random"])

    def forward(self, x1):
        v1 = ...  # Generate an input tensor of shape [..., ... , 2]

        if config["fallback_random"]:
            # Replace the function with its corresponding replacements
            v2 = torch.nn.functional.lowmem_dropout(...)

            # Revert to the original function
            self.linear = torch.nn.functional.dropout
        else:
            # Revert to the original function
            self.linear = torch.nn.functional.rand_like
        v3  = ...  # Generate a output tensor of shape [..., ... , 2]
        return v3


# Inputs to the model
x1 = torch.randn(40, 1, 10)
