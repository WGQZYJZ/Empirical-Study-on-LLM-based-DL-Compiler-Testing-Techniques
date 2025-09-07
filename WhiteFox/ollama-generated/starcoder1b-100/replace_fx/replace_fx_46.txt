
class Model(torch.nn.Module):
    def __init__(self, config):
        super().__init__()

        if config.fallback_random:
            self.linear = torch.nn.Linear(2, 2)
        else:
            self.config = config

            # Generate a random tensor
            # TODO: Check if the generated random tensor has valid shape for the Linear function
            # If not, raise an error. If yes, return.
            random_tensor = config.generate_random_tensor(
                config.num_layers, config.dim1, config.dim2)

            # Perform a swapping of dimensions 0 and 2 to get (2, dim1, dim2).
            random_swapped_tensor = torch.cat((
                random_tensor[:, :, 1:, :], random_tensor[:, :, :1, :]
            ), dim=2)

            self.linear = torch.nn.Linear(
                config.dim1, config.dim2, bias=False)
            
            # This is equivalent to the following line:
            # self.linear = torch.nn.Linear(
            #     config.dim1, config.dim2, bias=True)
            # The difference here is that the input of the first layer 
            # are swapped with (2, dim1, dim2). That corresponds to (3, 1, dim2), and
            # thus the Linear function in this case must use the output of the previous layer.
            self.linear.weight = torch.nn.Parameter(
                random_swapped_tensor)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2

