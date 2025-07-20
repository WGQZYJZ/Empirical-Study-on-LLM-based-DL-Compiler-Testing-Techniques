word_to_ix = {'hello': 0, 'world': 1}
embeds = torch.nn.Embedding(2, 5)
lookup_tensor = torch.tensor([word_to_ix['hello']], dtype=torch.long)
hello_embed = embeds(lookup_tensor)