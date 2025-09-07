
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.nn.functional.relu(v1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(64, 512).to('cuda:0')

 ## We will train the model for three epochs using the GPU.
epochs = 3; learning_rate = 0.0001; batch_size=64; momentum=0.9
 
## Define a loss function and optimizer 
loss = torch.nn.functional.mse_loss # MSE loss as an example of loss functions, please select another loss function that you are familiar with.
optimizer = optim.SGD(m.parameters(), lr=learning_rate)

for epoch in range(epochs):
    # Train the model using mini batches for each epoch 
    for batch_idx  in range(x1.shape[0] // batch_size + 1):
        optimizer.zero_grad() # clear gradients first, pytorch accumulates them otherwise
        x2 = x1[:batch_size * (epoch+1)] 
        y1  = m(x2) 
        loss_value  = loss(y1, y1) # compute the loss value
        loss_value.backward() # backpropogate to propagate the gradients
        optimizer.step() # update the weights using the computed gradients

# Generate and store an input tensor for model inference
x3 = torch.randn((batch_size*epochs), 512).to('cuda:0') 

