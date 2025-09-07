
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.matmul

    def forward(self, x1):
        query  = # TODO: Compute the query tensor using `x1` as the input.
        key  = # TODO: Compute the key tensor using `x1` as the input.
        attention_weights = # TODO: Compute the softmax of the scaled dot product between `query` and `key`,
        output = # TODO: Apply a weighted sum of `value` to get the output for each example in `batch`. 
        return output


# Initializing the model
m = Model()


def generate_input(batch_size, hidden_dim, num_heads):
    x1  = # TODO: Initialize the input tensor.
    return x1


x1  = generate_input(32, 64, 8)
