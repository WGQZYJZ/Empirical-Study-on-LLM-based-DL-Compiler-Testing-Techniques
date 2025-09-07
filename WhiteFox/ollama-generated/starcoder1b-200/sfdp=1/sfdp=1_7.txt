
class Model(torch.nn.Module):
    def __init__(self, hidden_size=512, num_heads=8):
        super().__init__()
        self.query  = torch.nn.Linear(768, hidden_size)
        self.key   = torch.nn.Linear(768, hidden_size)
        self.value = torch.nn.Linear(hidden_size, hidden_size)
        self.dropout_p = dropout_p

        self.layers = torch.nn.ModuleList([
            nn.Linear(hidden_size, hidden_size),  # Qk
            nn.LayerNorm(),
        ])
 
    def forward(self, qk):
        batch_size, sequence_length, input_size = qk.shape
        
        # Reshape the inputs to [batch * seq, channel, seq]
        qk_reshape = qk.view(batch_size*sequence_length, input_size)

        # Forward propagate Q and K into a concatenation of linear layers
        layer1 = self.query(qk_reshape).view(batch_size, sequence_length, -1)
        layer2 = self.key(qk_reshape).view(batch_size, sequence_length, -1)
        
        # Perform elementwise multiplication
        layer3 = torch.bmm(layer1, layer2).contiguous().view(-1, input_size)

        # Compute softmax to normalize output
        layer4 = nn.functional.softmax(layer3, dim=-1)  # Qk

        # Forward propagate Q and K into a dot product of the Qk values
        layer5 = torch.bmm(qk_reshape, layer4).contiguous().view(-1, input_size)

        # Apply dropout to the softmax output
        layer6 = nn.functional.dropout(layer5, p=self.dropout_p)  # Qk
        
        # Forward propagate Q and K into a dot product of the Qk values again
        layer7 = torch.bmm(qk_reshape, layer4).contiguous().view(-1, input_size)

        # Apply dropout to the softmax output
        layer8 = nn.functional.dropout(layer7, p=self.dropout_p)  # V

        # Forward propagate Q and K into a dot product of the Qk values again
        layer9 = torch.bmm(qk_reshape, layer4).contiguous().view(-1, input_size)
        
        # Compute error function by multiplying the Qk values by the output of the hidden layers
        layer10 = (layer9 - layer8) * layer4

        # Apply dropout to the dot product output and value tensor
        layer11 = nn.functional.dropout(layer10, p=self.dropout_p)  # E

        # Forward propagate Qk dot product with values to get hidden layer outputs
        self.layers[-1].bias.data.zero_()
        layer12 = torch.bmm(qk_reshape, layer11).contiguous().view(-1, self.layers[-1].out_features)  # H

        return self.layers[-1](layer12)


# Initializing the model
m = Model()


