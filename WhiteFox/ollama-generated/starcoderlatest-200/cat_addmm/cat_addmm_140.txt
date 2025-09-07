
class Model(torch.nn.Module):
    def __init__(self, hidden_size=64):
        super().__init__()
        self.linear = torch.nn.Linear(3 * 64 * 64, hidden_size)
 
    def forward(self, x1):
        t1 = F.relu(torch.addmm(x1.view(-1,3*64*64), torch.eye(3).view(3,1)*0.5, torch.eye(3).view(3,3)))
        t2 = t1.view(t1.shape[0], -1)  # Flatten the result of the activation function into a single column vector. Use the view function to reshape the input tensor as if it had n elements. For example, consider the following tensors: [batch_size x channels x height x width]. Viewing the element at index (5,32,64) from the 0th batch will provide all of those values in a single row vector of length equal to (64*64*3). By reshaping the input tensor to have n elements and concatenating along dimension = 1, this reshape operation will return a vector whose n-element form is (n=1 x m=64*64*3) which we can use as an element in a column of a matrix.
        t3 = self.linear(t2)
        return F.relu(t3)
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3*64*64)
