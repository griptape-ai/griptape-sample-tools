// import { griptapeApiBase as api } from "./griptapeApiBase";
// const injectedRtkApi = api.injectEndpoints({
//   endpoints: (build) => ({
//     createAssistant: build.mutation<
//       CreateAssistantApiResponse,
//       CreateAssistantApiArg
//     >({
//       query: (queryArg) => ({
//         url: `/assistants`,
//         method: "POST",
//         body: queryArg.createAssistantRequestContent,
//       }),
//     }),
//     deleteAssistant: build.mutation<
//       DeleteAssistantApiResponse,
//       DeleteAssistantApiArg
//     >({
//       query: (queryArg) => ({
//         url: `/assistants/${queryArg.assistantId}`,
//         method: "DELETE",
//       }),
//     })
// export type CreateAssistantApiResponse =
//   /** status 201 CreateAssistant 201 response */ CreateAssistantResponseContent;
// export type CreateAssistantApiArg = {
//   createAssistantRequestContent: CreateAssistantRequestContent;
// };
// export type DeleteAssistantApiResponse =
//   /** status 204 DeleteAssistant 204 response */ void;
// export type DeleteAssistantApiArg = {
//   assistantId: string;
// };
// export const {
//   useCreateAssistantMutation,
//   useDeleteAssistantMutation,
  
// } = injectedRtkApi;
