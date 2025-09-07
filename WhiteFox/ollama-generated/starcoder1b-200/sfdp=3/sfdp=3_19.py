The input tensor for each model is the same as the input of the previous models in a particular scenario. The difference here is that the input for the second model does not have a fixed value. It depends on the actual context and the inputs to the model.


# Model
class Model(torch.nn.Module):
    def __init__(self, n=None):
        super().__init__()
        self.n = n
 
    def forward(self, x1, x2):
        x  = torch.cat([x1, x2], dim=1)
        w  = torch.nn.Linear(self.n, self.n).weight
        b  = torch.nn.Linear(self.n, self.n).bias
        m  = torch.matmul(w, x) + b  # Apply matrix multiplication with the weights and the inputs
        m1 = (m * w).add_(b)  # Add biases for the output tensor
        m2 = m1.mul(torch.nn.functional.softmax(x1 * x2, dim=-1))  # Apply softmax function to the outputs
        return m2


# Initializing the model
m = Model()
The input for each model is concatenated before they are fed into a linear layer with an identical number of nodes as the input shape, and then two matrices multiply with the same shape (one matrix multiplying with another, while the shapes don't match). The output of these models are softmax applied to the dot product of the first and second model output tensors.


# Model
class Model(torch.nn.Module):
    def __init__(self, d_k=None, n_head=1, n_layer=2):
        super().__init__()
        self.d_k = d_k
        self.n_head = n_head
        self.n_layer = n_layer
 
    def forward(self, x1, x2):
        wq  = torch.nn.Linear(d_k, d_k * self.n_head)  # Embedding layer for query vector projections
        vk  = torch.nn.Linear(d_k, d_k * self.n_head)  # Embedding layer for key vector projections
        vw  = torch.nn.Linear(d_v, d_v * self.n_head)  # Embedding layer for value vector projection
