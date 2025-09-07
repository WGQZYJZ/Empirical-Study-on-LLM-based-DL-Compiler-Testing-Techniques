
class EncoderLayer(nn.Module):
    def __init__(self, d_model, selfattn, feedforward, dropout):
        super().__init__()
        
        # Implementation of Feed Forward Network with activation function 'gelu'
        self._selfattn  = selfattn 
        self._feedforward  = feedforward 
        self._dropout  = nn.Dropout(dropout)
        
    def forward(self, x):
        output_1 = self._selfattn(x)  # Compute the dot product of the query and key, and scale it
        output_2  = self._dropout(output_1)  # Apply dropout to the softmax output
        output_3 = torch.add(output_2, x)   # Add the attention mask to the scaled dot product

        # Apply dropout to the feed forward network's output 
        output_4  = self._dropout(self._feedforward(x))

        return torch.add(output_3, output_4)

# Initializing the model
encoderLayer1 = EncoderLayer(512, MultiHeadedAttention(10), FeedForward(d_model=512, dropout=0.1).apply, dropout=0.1)


# Inputs to the model
x1  = torch.rand(32, 48960, requires_grad=True).to('cuda') # Input to the feed forward network
__output__  = encoderLayer1(x1)  # Output of the feed forward network

