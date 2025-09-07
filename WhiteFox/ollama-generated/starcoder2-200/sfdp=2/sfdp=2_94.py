
class Model(torch.nn.Module):
    def __init__(self, embedding_size, num_layers, hidden_size):
        super().__init__()
        self.encoder  = torch.nn.LSTM(
            input_size=embedding_size, 
            hidden_size=hidden_size, 
            num_layers=num_layers,  
            dropout=0.1)
 
    def forward(self, x): 
        return self.encoder(x)[-1][0] # Extract the last element of a sequence of tensors and then return its first element.


# Initializing the model
m  = Model()

# Inputs to the model
__inputs__  = torch.randn(256, 8, 3)

# Calling the model with the inputs
outputs  = m(__inputs__) # <p:input>

