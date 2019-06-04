from ClassLawrMongoDB import MongoDB

Test = MongoDB("mongodb+srv://Admin:P13hesheshes@botonlnr-h6f2t.mongodb.net/test?retryWrites=true&w=majority")


Test.nice_print(Test.show_database('Test'))
print(Test.check_collection('Test', 'URL'))

Test.clear_collection('Test', 'URL')

Test.add_line_to_end('Test', 'URL', {'name': 'user 1', 'level': 1})
Test.add_line_to_end('Test', 'URL', {'name': 'user 2', 'level': 2})
Test.add_line_to_end('Test', 'URL', {'name': 'user 3', 'level': 3})

Test.nice_print(Test.show_collection('Test', 'URL'))

Test.delete_collection('Test', '111')
Test.clear_collection('Test', 'URL')
Test.nice_print(Test.show_collection('Test', 'URL'))


Test.add_line_to_end('Test', 'URL', {'name': 'user 1', 'level': 1})
Test.add_line_to_end('Test', 'URL', {'name': 'user 2', 'level': 2})
Test.add_line_to_end('Test', 'URL', {'name': 'user 3', 'level': 3})

Test.del_line_to_end('Test', 'URL')
Test.nice_print(Test.show_collection('Test', 'URL'))

