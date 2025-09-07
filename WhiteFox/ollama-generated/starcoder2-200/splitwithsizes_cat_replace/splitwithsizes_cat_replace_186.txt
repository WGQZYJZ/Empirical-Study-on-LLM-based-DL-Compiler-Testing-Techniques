
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):

        # Split the input tensor along dimension 2 with split sizes [3] and [5], and concatenate them together along dimension 0
        split_tensors = torch.split(x1, [3, 5], dim=0)
        concatenated_tensor = torch.cat([split_tensors[i] for i in range(len(split_tensors))], 0)

        return concatenated_tensor


# Initializing the model
m = Model()
 
# Input tensor for the model initialization
input_tensor = torch.rand((1, 256, 397))

# Feeding input to the model and storing the output in __output__ variable
__output__  = m(input_tensor)

