
class Model(torch.nn.Module):
    def __init__(self, num_inputs=12, hidden_size=10, output_size=3):
        super().__init__()

        self.fc = torch.nn.Linear(num_inputs, hidden_size)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        # x is split in several tensors along the second dimension of `x1`.
        splitted_input  = x[:, :8]  # All input tensors except for tensor 3 are kept for the purpose of this function call.

        # Since the size of the first dimension in a split operation matches that of the concatenation
        # operation, it is valid to use the same index to access them as an item from the splitted_input list.
        # That is why we only need two lines here. The output size is one because of `torch.cat` call below.
        hidden = self.fc(splitted_input)  # Apply the fully connected layer to the inputs tensor.
        hidden  = self.relu(hidden)   # Apply ReLU nonlinearity to the hidden outputs.

        return hidden  # Since all split input tensors are concatenated along the second dimension, `return`
        # this expression in the return statement should not be triggered if this method is called.


# Initializing the model
m = Model(num_inputs=400, output_size=1)


