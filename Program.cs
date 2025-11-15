using System;
using System.IO;
using Microsoft.Data.Sqlite;
using System.Diagnostics;
using System.Threading.Tasks;
namespace RecupInventarios
{
    class Program
    {
        static void Main(string[] args)
        {
            var stopwatch = Stopwatch.StartNew();
            string nome = args.GetValue(0).ToString().Replace(".db",".sql");
            Console.WriteLine($"Inicio do Ficheiro {args.GetValue(0)}");
            StreamWriter output = new StreamWriter(nome);
            output.AutoFlush = true;
            using (var connection = new SqliteConnection($"Data Source={args.GetValue(0)}"))
            {
                connection.Open();
                var command = connection.CreateCommand();
                command.CommandText =
                @"SELECT *FROM InventoryDetails where Picado = '1'";
                using (var reader = command.ExecuteReader())
                {
                    while (reader.Read())
                    {
                        var InvID = reader.GetString(0);
                        var QTY = reader.GetString(9);
                        output.WriteLine($"Update Ekanban.Inventario_det Set Qt_inventariada = '{QTY}', picado = '1' where id = {InvID} and Picado !='1'");
                    }
                }
            }
            output.Close();

            stopwatch.Stop();

            // Output total time in milliseconds
            Console.WriteLine($"Total execution time: {stopwatch.ElapsedMilliseconds} ms");
            Console.WriteLine($"Precise time: {stopwatch.Elapsed.TotalMilliseconds} ms");
            Console.WriteLine($"Concluido no ficheiro {nome}");
            Console.ReadLine();
        }
    }
}
