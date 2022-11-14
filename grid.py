s_row = ['.xxxx.', 'xxxxxx', 'xxx...', '.xxxx.', '...xxx', '....xx', 'xxxxxx', '.xxxx.']
a_row = ['.xxxx.', 'xxxxxx', 'xx..xx', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx']
m_row = ['x....x', 'xx..xx', 'xxxxxx', 'xxxxxx', 'xx..xx', 'xx..xx', 'xx..xx', 'xx..xx']

sam_row_test = []
sam_row_test.append(s_row[0] + '--' + a_row[0] + '--' + m_row[0])
sam_row_test.append(s_row[1] + '--' + a_row[1] + '--' + m_row[1])
sam_row_test.append(s_row[2] + '--' + a_row[2] + '--' + m_row[2])
sam_row_test.append(s_row[3] + '--' + a_row[3] + '--' + m_row[3])
sam_row_test.append(s_row[4] + '--' + a_row[4] + '--' + m_row[4])
sam_row_test.append(s_row[5] + '--' + a_row[5] + '--' + m_row[5])
sam_row_test.append(s_row[6] + '--' + a_row[6] + '--' + m_row[6])
sam_row_test.append(s_row[7] + '--' + a_row[7] + '--' + m_row[7])

print(*sam_row_test, sep = "\n")