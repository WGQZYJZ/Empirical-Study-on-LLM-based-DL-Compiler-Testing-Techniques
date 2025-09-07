
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, scale_factor=0.5148973265973928, dropout_p=0.2, value=None): 
        v1  = torch.nn.functional.linear(query)
        v2  = v1 * 0.0 + self.embedding_table.clone().detach()[:self.hidden_size]
        v3  = key.transpose(-2, -1)
        v4  = query @ v3
        v5  = scale_factor
        v6  = v4 * v5
        v7  = torch.nn.functional.softmax(v6, dim=-1)
        v8  = self.dropout(v7)
        return v2 @ v8


# Initializing the model
m = Model()
 
# Inputs to the model
q = torch.randn(3000, 500, requires_grad=True)
k = torch.randn(15000, 49967, 528, requires_grad=True)

# Initializing optimizer
opt = torch.optim.SGD([q], lr=0.03)
 
# Training the model for 2 epochs
for epoch in range(2):
    for i in range(100):
        # Set the gradient to be zero before computing the gradient
        opt.zero_grad()
        # Generate target output based on the input tensors and the initialized model m
        y = m(q, k)
        # Compute the loss function with the given target output
        loss = torch.sum((y - 2)**2)
        # Compute the gradient of the given loss variable wrt all learnable parameters using backpropagation algorithm
        loss.backward()
        # Take a single optimization step using Stochastic Gradient Descent
        opt.step()