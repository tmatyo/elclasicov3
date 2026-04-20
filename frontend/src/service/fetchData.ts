import { UseFetchResult } from "@/types/app";

export async function useFetchData<T>(url?: string): Promise<UseFetchResult<T>> {
	if (!url) {
		url = `${process.env.API_ENDPOINT}${process.env.API_GET_DATA}`;
		if (!process.env.API_ENDPOINT || !process.env.API_GET_DATA) {
			return { data: null, error: new Error("API endpoint is not defined") };
		}
	}

	let result = { data: null, error: null } as UseFetchResult<T>;

	try {
		const response = await fetch(url);
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		result.data = await response.json();
	} catch (e: unknown) {
		if (e instanceof Error) {
			result.error = e;
		}
	}
	return result;
}
