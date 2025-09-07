
class Model(torch.nn.Module):
    def __init__(self, embedding_dim=128, nhead=8, num_hidden_layers=2):
        super().__init__()
        self.pos_embedding = torch.nn.Embedding(embedding_dim * 2 + 2, embedding_dim) # position embedding for queries and keys plus two additional positions [CLS], [SEP]
        self.self_attn = torch.nn.MultiheadAttention(embed_dim=embedding_dim, num_heads=nhead, batch_first=True) # self attention layer
        self.linear1 = torch.nn.Linear(embedding_dim * 2 * nhead, embedding_dim) # linear projection of the sequence outputs from the attention and position embeddings into a d-dimensional space
        self.dropout = torch.nn.Dropout(p=0.35)
        self.linear2 = torch.nn.Linear(embedding_dim, embedding_dim) # linear projection to a final output with dropout

        for layer in range(num_hidden_layers):
            setattr(self, f'layer_{layer}', torch.nn.Sequential(
                torch.nn.Dropout(p=0.2), # apply dropout to the sequence outputs of the previous layer
                torch.nn.Linear(embedding_dim, embedding_dim * 4), # linear projection with a dimension of d*4 times its original dimension
                torch.nn.GELU(), # GELU nonlinearity (implementation of GeLU: Gaussian Error Linear Units)
                torch.nn.Dropout(p=0.2), # apply dropout to the sequence outputs
            ))

        self.output_layer = torch.nn.Linear(embedding_dim * 4, embedding_dim * 8)
        self.classifier = torch.nn.Sequential(torch.nn.Dropout(),torch.nn.Linear(embedding_dim*4,1))

    def forward(self, x):
        # input: x (batch_size, num_seq_per_example, input_seq_length, embedding_dim)
        
        # query and key: q (batch_size, num_seq_per_example, embedding_dim), k (batch_size, num_seq_per_example, embedding_dim)
        query = torch.stack([x[i].unsqueeze(0).repeat((1,query_len,1)) for i in range(batch_size)], dim=0) # [batch_size * num_queries, query_length, d]
        key = torch.stack([x[j].unsqueeze(0).repeat((1,1,key_len)) for j in range(batch_size)], dim=0)

        # position embeddings: pos (batch_size, 2 * embedding_dim), p0 and p1 (1, embedding_dim)
        pos = self.pos_embedding(torch.tensor([i+j*2 for i in range(query_len) for j in range(key_len)]).long()) # [2 * query_length * key_length, embedding_dim]
        p0 = torch.zeros((1,query_len), dtype=torch.float32) + 1e-8 # p0 (batch_size, query_length), where all values are initialized to 1e-8 (i.e., 1/512)
        p0[:, 0::2] = -1e-8 # p0[i][j] is initially -1e-8 if i is odd and j is even, otherwise it is initialized to 0.0
        p0 = torch.cat((p0, torch.zeros((1,key_len), dtype=torch.float32)), dim=-1) # Concatenate the position embeddings of [CLS] and [SEP] as last values in pos
        p1 = -pos.permute(0, 2, 1).contiguous().view(-1, embedding_dim)[-1:] # Create position embeddings for the key tensor by taking the last value of each row (i.e., the last position in every sequence) and concatenating it to the rest of the values

        # self attention layer: s (batch_size, num_seq_per_example, query_len, embedding_dim * nhead), qk (batch_size, num_seq_per_example, query_len, embedding_dim)
        s = torch.stack([self.layer_0(x).unsqueeze(-1).repeat((1,1,1,8)) for x in [query, key]], dim=0) # [batch_size * 2, query_length, input_seq_length, embedding_dim]
        qk = torch.cat([s[i].view(-1, self.embedding_dim * nhead, s[i].shape[-1]) for i in range(batch_size)], dim=0) # Concatenate the sequence outputs of all examples into a single tensor (i.e., [query length * key length * d, embedding_dim*nhead])
        qk = self.self_attn(qk, p0 + torch.ones_like(p0), p1)[0] # Self attention layer with queries (the output of the last convolution) and keys, where queries are initialized to be all ones (i.e., [query length * key length * d, embedding_dim*nhead])
        s = qk / 3 # Scale values by 0.3

        # position embeddings: pos (batch_size, 2 * embedding_dim), p0 and p1-->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->->