
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qk = torch.nn.Linear(512, 2048) # Create a linear layer with 512 hidden units and 2048 output units (note the use of a Linear module here instead of a Sequential module as per [here](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)).
        self.v = torch.nn.Linear(2048, 1)  # Create a linear layer with 2048 hidden units and 1 output unit (note the use of a Linear module here instead of a Sequential module as per [here](https://pytorch.org/docs/stable/generated/torch.nn.Linear.html)).

    def forward(self, x1):
        # Compute the dot product of the query and key tensors.
        qk = self.qk(x1)  # We can also use `self.qk(x1).view(x1.shape[0], -1)` to avoid a reshape
        scaled_qk = qk.mul(scale_factor)  # Scale the dot product by a factor

        # Apply softmax over the scaled dot product (a vectorized version of dot(query, key)) and dropout.
        softmax_qk = scaled_qk.softmax(-1)
        dropout_qk = torch.nn.functional.dropout(softmax_qk, p=dropout_p)

        # Compute the output by computing the dot product of the dropout output and the value tensor (a vectorized version of dot(dropout output, value)).
        output = dropout_qk.matmul(value)  # Finally, compute the result as `output = qk.transpose(-2, -1).matmul(value)`.

        return output


# Initializing the model
m = Model()


