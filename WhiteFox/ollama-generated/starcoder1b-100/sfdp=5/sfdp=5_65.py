
class Model(torch.nn.Module):
    def __init__(self, args, hidden_size=128, num_heads=8, max_len=100, vocab_size=50):
        super().__init__()
        self.conv = torch.nn.Conv1d(vocab_size, 32, kernel_size=3, stride=1) # Embedding of the word-ids and hidden_state are concatenated together
        self.fc   = torch.nn.Linear(hidden_size*4, hidden_size//8, bias=True)
        self.fc2  = torch.nn.Linear(hidden_size//8, vocab_size) # Final hidden state is linearly transformed to output the logits of softmax
        self.attn  = TransformerSelfAttention(args.dropout_p)
        self.rnn   = torch.nn.GRU(vocab_size, hidden_size, batch_first=True, num_layers=2, bidirectional=False)

    def forward(self, input):
        x = self.conv(input) # Embedding of the word-ids and hidden_state are concatenated together

        h0 = torch.zeros((2, 1, self.args.hidden_size))
        c0 = torch.zeros((2, 1, self.args.hidden_size))
        x = self.rnn(x.view(-1, x.size(-1)), h0, c0)

        hidden_states = x[-1] # The last output of GRU is the last hidden state of the decoder
        logits = self.fc(hidden_states.contiguous().view(-1, hidden_size*4))
        out         = F.log_softmax(self.fc2(logits), dim=-1)

        return out


# Initializing the model
m = Model(args)

# Inputs to the model
inputs = torch.tensor([768]) # Tensor for input data
