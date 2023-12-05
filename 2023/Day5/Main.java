import java.io.*;
import java.util.*;
// Part 2 Brute Force
public class Main {
    static long mapThroughCategories(long number, List<long[]> mappings) {
        for (long[] mapping : mappings) {
            number = mapNumber(mapping, number);
        }
        return number;
    }
    static long mapNumber(long[] mapping, long number) {
        for (int i = 0; i < mapping.length; i += 3) {
            long destStart = mapping[i];
            long srcStart = mapping[i + 1];
            long length = mapping[i + 2];
            if (number >= srcStart && number < srcStart + length) {
                return destStart + (number - srcStart);
            }
        }
        return number;
    }
    static long[] addToMap(long[] mapping, long[] newEntry) {
        long[] newMapping = Arrays.copyOf(mapping, mapping.length + 3);
        System.arraycopy(newEntry, 0, newMapping, mapping.length, 3);
        return newMapping;
    }
    public static void main(String[] args) throws IOException {
        List<long[]> mappings = new ArrayList<>();
        List<Long> seedRanges = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader("input.txt"))) {
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.startsWith("seeds:")) {
                    String[] parts = line.substring(7).split(" ");
                    for (String part : parts) {
                        seedRanges.add(Long.parseLong(part));
                    }
                } else if (line.contains("map:")) {
                    mappings.add(new long[0]);
                } else if (!line.isEmpty() && !mappings.isEmpty()) {
                    String[] parts = line.split(" ");
                    long[] mapEntry = {Long.parseLong(parts[0]), Long.parseLong(parts[1]), Long.parseLong(parts[2])};
                    int lastIdx = mappings.size() - 1;
                    mappings.set(lastIdx, addToMap(mappings.get(lastIdx), mapEntry));
                }
            }
        }
        long lowestLocation = Long.MAX_VALUE;
        for (int i = 0; i < seedRanges.size(); i += 2) {
            long start = seedRanges.get(i);
            long length = seedRanges.get(i + 1);
            for (long j = start; j < start + length; j++) {
                long location = mapThroughCategories(j, mappings);
                if (location < lowestLocation) {
                    lowestLocation = location;
                }
            }
        }
        System.out.println(lowestLocation);
    }
}
