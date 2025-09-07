
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.linear.weight, self.linear.bias)
        bn1 = torch.nn.functional.batch_norm(v1, training=False)  # Bn1 can be used for a batch norm layer, and this line is the same as:
        output = bn1(v1, True)  # If it's not specified whether to return Bn1 or output, then Bn1 is used by default. This means that if the module was trained, then BN will update the running statistics of the batch norm layer, and use these statistics to get the final results (i.e., the value of the output).
        return output


# Initializing the model
m = Model()


