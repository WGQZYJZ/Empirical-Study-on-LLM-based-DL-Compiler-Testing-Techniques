
class Model(torch.nn.Module):
    def __init__(self, num_inputs = 3):
        super().__init__()

        self.linearA = torch.nn.Linear(num_inputs, 2) # Number of inputs for linearA matches the number of permuted input tensors
        self.linearB = torch.nn.Linear(2, 10) # Number of outputs in linearB is set higher than the number of output columns in permuted tensors

        self.linear1  = torch.nn.Linear(num_inputs + 5, 3*4) # Number of input and output columns are set based on the number of permuted tensors
        self.linear2  = torch.nn.Linear(3*4 + num_inputs/2, num_inputs * num_inputs)

    def forward(self, x1):

        t1 = x1.permute(0, 2, 1) # Permute the input tensors
        t2 = self.linearA(t1)

        t3 = torch.bmm(x1.T, t2[:, :, None]) # BMM requires three tensors on the left side as inputs, but in our example we only have one tensor, thus this tensor becomes 5-dimensional. Thus the bmm function is invoked on an input with 5 dimensions.

        t4 = torch.nn.functional.linear(x1[:, :, None], self.linear2) # BMM and linear functions work fine with 3D inputs

        t5 = x1 + x1 + x1

        return t1, t2, t3


# Initializing the model