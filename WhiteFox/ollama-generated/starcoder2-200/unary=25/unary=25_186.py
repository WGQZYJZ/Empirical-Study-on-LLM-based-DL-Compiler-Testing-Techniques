
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       v1 = torch.randn(32)
       b = 0
       for i in range(5):
           t1 = v1 > b
           v2 = v1 * -2
           v4 = torch.where(t1, v1, v2)
           v1 = v4
           b += 1
       return v4


# Initializing the model
m  = Model()
 
# Input to the model
input_tensor = torch.randn(32)
 
# Initializing variables for forward pass
v1, t1, b  = input_tensor.clone(), [], 0
 
for i in range(5):
    # Generating the boolean tensor corresponding to each element of v1 > 0
    t1 += [v1 > b]
    # Creating a new tensor that contains the output of the multiplication by -2 where v1 is greater than or equal to 0, and 0 otherwise.
    v4 = torch.where(t1[-1], v1, v1*-2)
    v1 = v4
    b += 1
 
# Printing final output from the model (same as __output__ in the previous question)
print(v1)
 
