
class Model(torch.nn.Module):
    def __init__(self, input1, input2):
        super().__init__()

    def forward(self, x):
        t = torch.cat([x.data[0], self.linear.weight])  # Concatenate tensors along a dimension
        t_v  = torch.nn.functional.linear(t, self.linear.weight, self.linear.bias)  # Apply linear transformation to the concatenated tensor.
        return x


# Initializing the model
model1 = Model()


class Model2(torch.nn.Module):
    def __init__(self, input3):
        super().__init__()

    def forward(self, t):
        t = torch.cat([t[0], t])  # Concatenate tensors along a dimension

        # Apply pointwise unary operation to the concatenated tensor.
        t1_v2 = torch.nn.functional.relu(torch.max(torch.abs(t), self._activation_input_threshold))
        return x


# Initializing the model
model2 = Model2()


