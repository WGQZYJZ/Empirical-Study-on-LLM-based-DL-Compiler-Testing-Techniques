
class Model(torch.nn.Module):
    def __init__(self, input_vocab_size, target_vocab_size, embedding_dim, hidden_dim):
        super().__init__()
        self.embedding  = torch.nn.Embedding(input_vocab_size, embedding_dim)
        self.conv1      = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.attention  = torch.nn.Linear(hidden_dim, hidden_dim)
        self.dropout    = torch.nn.Dropout(0.5)
        self.fc         = torch.nn.Linear(hidden_dim, target_vocab_size)
 
    def forward(self, input_tensor, targets):
        embed        = self.embedding(input_tensor).view(-1, 3 * embedding_dim)
        conv_output = F.relu(self.conv1(embed))
        #print(f'Conv output shape {conv_output.size()}')
 
        x = conv_output.contiguous().view(-1, hidden_dim)
        #print(f'X shape {x.size()}')
        h = self.attention(h).view(-1, targets.shape[0], 1)
        #print(f'H shape {h.size()}')
        x = x * h[:, :, None]
        #print(f'X multiplied by H shape {x.size()}')
        x = x + self.dropout(conv_output.contiguous().view(-1, hidden_dim))
        #print(f'Adding the output of the dropout operation to the model shape {x.size()}')
        x = F.log_softmax(self.fc(x), dim=-1)
        #print(f'Final output shape {x.size()}')
        return x


