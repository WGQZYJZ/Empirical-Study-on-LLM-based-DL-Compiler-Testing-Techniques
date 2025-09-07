
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.q_linear = torch.nn.Linear(768, 1024)
        self.k_linear = torch.nn.Linear(768, 1024)
        self.v_linear = torch.nn.Linear(768, 1024)
 
    def forward(self, x1):
        # Query
        q = F.relu(self.q_linear(x1))
        
        # Key
        k = F.relu(self.k_linear(x1))

        # Value
        v = F.relu(self.v_linear(x1))

        # Compute dot product
        kq = torch.matmul(k, q)  # The dot product is computed between the weight matrices of the two tensors in the form of a matrix.

        # Scale
        kq *= self.scaling_factor

        # Softmax over the dot product to get the normalized attention weights.
        softmax_qk = kq.softmax(-2)  # The softmax function computes log(exp(dot-product)) / sum(exp(dot-product)) where exp is element-wise operation, and sum is element-wise addition operation on all dimensions.

        # Dropout to protect the attention from undesirable features of training
        dropout_qk = F.dropout(softmax_qk, p=self.dropout)  # The dropout function randomly samples input values of a given shape, and it makes sure that the input value can be recognized by certain types of neural network layers and activation functions.

        # Output
        output = torch.matmul(dropout_qk, v)  # A dot product is computed between the weight matrices of the two tensors in the form of a matrix.
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 768)
